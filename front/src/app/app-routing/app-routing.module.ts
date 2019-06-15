import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { WritingsComponent } from '../writings/writings.component';

const routes: Routes = [
  {
      path:  '',
      redirectTo:  '',
      pathMatch:  'full',
  },
  {
      path:  'writings',
      component:  WritingsComponent,
  },
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})
export class AppRoutingModule { }
