import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-my-outer',
  templateUrl: './my-outer.component.html',
  styleUrls: ['./my-outer.component.css'],
})
export class MyOuterComponent {
    mytotal: number = 0;

    handleInnerPlusChange() {
        this.mytotal += 10;
    }

    handleInnerMinusChange() {
        this.mytotal -= 10;
    }
}