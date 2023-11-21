// my-inner.component.ts

import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css'],
})
export class MyInnerComponent {
  innerTotal = 5;
  @Input() total: number = 0;
  @Output() totalChange = new EventEmitter<number>();

  clickPlus() {
    this.innerTotal += 1;

    if (this.innerTotal > 9) {
      this.innerTotal = 0;
      this.total += 10;
    }

    this.totalChange.emit(this.total); 
  }

  clickMinus() {
    this.innerTotal -= 1;

    if (this.innerTotal < -9) {
      this.innerTotal = 0;
      this.total -= 10;
    }

    this.totalChange.emit(this.total);
  }
}
