import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Issues } from '../issues';
import { IssuesService } from '../issues.service';
import { Output, EventEmitter } from '@angular/core';

interface IssueForm {
  title: FormControl;
  description: FormControl;
  priority: FormControl;
  type: FormControl;
}

@Component({
  selector: 'app-issue-report',
  templateUrl: './issue-report.component.html',
  styleUrls: ['./issue-report.component.css']
})
export class IssueReportComponent {
  @Output() formClose = new EventEmitter();
  issueForm = new FormGroup<IssueForm>({
    title: new FormControl('', Validators.required),
    description: new FormControl('', Validators.required),
    priority: new FormControl('', Validators.required),
    type: new FormControl('', Validators.required),
  });

  constructor(private issueService: IssuesService) {}

  addIssue() {
    if (this.issueForm.valid) {
      this.issueService.createIssue(this.issueForm.getRawValue() as Issues);
    }
    this.formClose.emit();
  }
}
