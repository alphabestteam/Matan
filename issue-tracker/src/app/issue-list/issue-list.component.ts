import { Component, OnInit } from '@angular/core';
import { Issues } from '../issues';
import { IssuesService } from '../issues.service';

@Component({
  selector: 'app-issue-list',
  templateUrl: './issue-list.component.html',
  styleUrls: ['./issue-list.component.css']
})
export class IssueListComponent implements OnInit{
    issues: Issues[] = [];
    showReportIssue = false;

    constructor(private issuesService: IssuesService){}

    ngOnInit(): void {
        this.getIssues();
    }

    private getIssues() {
        this.issues = this.issuesService.getPendingIssues();
    }

    onCloseReport() {
        this.showReportIssue = false;
        this.getIssues();
    }
}
