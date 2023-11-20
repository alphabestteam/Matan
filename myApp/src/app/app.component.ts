import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  myForm: FormGroup;
  
  constructor(private formBuilder: FormBuilder) {
    this.myForm = this.formBuilder.group({
      username: ['', [Validators.required, Validators.minLength(2), Validators.maxLength(20)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(10)]],
    });
  }

  onSubmit() {
    if (this.myForm.valid) {
      console.log(this.myForm.value);
    } else {
      console.log(this.myForm);
    }
  }
}
