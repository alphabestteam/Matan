import { Component } from '@angular/core';
import { MyInnerComponent } from '../my-inner/my-inner.component';

@Component({
  selector: 'app-my-outer',
  templateUrl: './my-outer.component.html',
  styleUrls: ['./my-outer.component.css']
})
export class MyOuterComponent {
    total = 0;

    onTenEventTriggered(event: boolean) {
        if(event){
            this.total += 10;
        } else {
            this.total -= 10;
        }
    }
}