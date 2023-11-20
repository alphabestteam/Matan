import { Component } from '@angular/core';
import { FILMS } from '../star-wars-fake-db/film-data';
import { MovieCardComponent } from '../movie-card/movie-card.component';

@Component({
  selector: 'app-starwars',
  templateUrl: './starwars.component.html',
  styleUrls: ['./starwars.component.scss']
})
export class StarwarsComponent {
    FILMS = FILMS;
}
