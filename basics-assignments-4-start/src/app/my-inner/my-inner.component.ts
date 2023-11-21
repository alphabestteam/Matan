import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css'],
})
export class MyInnerComponent {
  @Input() innerTotal: number = 0;
  @Output() innerPlusChange = new EventEmitter<number>();
  @Output() innerMinusChange = new EventEmitter<number>();

  clickPlus() {
    this.innerTotal += 1;

    if (this.innerTotal > 9) {
      this.innerTotal = 0;
      this.innerPlusChange.emit(this.innerTotal + 10);
    }
  }

  clickMinus() {
    this.innerTotal -= 1;

    if (this.innerTotal < -9) {
      this.innerTotal = 0;
      this.innerMinusChange.emit(this.innerTotal - 10);
    }
  }
}