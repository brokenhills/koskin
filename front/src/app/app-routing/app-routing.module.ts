import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { WritingsComponent } from '../writings/writings.component';
import { GalleryComponent } from '../gallery/gallery.component';

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
  {
    path:  'gallery',
    component:  GalleryComponent,
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
