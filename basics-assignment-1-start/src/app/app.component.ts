import { Component } from '@angular/core';
import { SuccessAlertComponent } from './success-alert/success-alert.component';
import { WarningAlertComponent } from './warning-alert/warning-alert.component';
import { MatFormField } from '@angular/material/form-field';
import { MatSelect } from '@angular/material/select';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    indicator: boolean;
    pageClick = false;
    selectedNumber: number;
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    
    onClickPlus(){
        this.indicator = true;
        this.pageClick = true;
    }

    onClickMinus(){
        this.pageClick = true;
        this.indicator = false;
    }

    getNumberRange(num: number): number[] {
        return Array.from({ length: num }, (_, index) => index + 1);
    }
}
