import { Component } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css'],
})
export class MyInnerComponent {
    total = 5;
    @Output() tenEvent = new EventEmitter<boolean>();

    clickPlus() {
        this.total += 1;

        if(this.total > 9){
            this.total = 0;
            this.tenEvent.emit(true);
        }
    }

    clickMinus() {
        this.total -= 1;

        if(this.total < -9){
            this.total = 0;
            this.tenEvent.emit(false);
        }
    }
}
