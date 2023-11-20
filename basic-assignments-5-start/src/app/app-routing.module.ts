import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StarwarsComponent } from './starwars/starwars.component';

const routes: Routes = [{ path: 'star-wars-movies', component: StarwarsComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
