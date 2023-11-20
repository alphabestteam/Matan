import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    title = 'Display Details';
    content = 'Secret Password = tuna';
    array = [];
    counter = 0;

    click(){
        this.counter++;

        if(this.content == ""){
            this.content = "Secret Password = tuna";
        } else {
            this.content = "";
        }

        this.array.push(this.counter);
    }
}
