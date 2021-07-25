import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { WritingsComponent } from '../writings/writings.component';
import { GalleryComponent } from '../gallery/gallery.component';
import { WritingComponent } from '../writing/writing.component';
import { MainComponent } from '../main/main.component';

const routes: Routes = [
  {
    path:  '',
    redirectTo:  'main',
    pathMatch:  'full',
  },
  {
    path:  'main',
    component:  MainComponent,
    children: [
      {
        path:  'liked/:id',
        component:  WritingComponent,
      },
    ]
  },

  {
    path:  'writings',
    component:  WritingsComponent,
    children: [
      {
        path: "writing/:id",
        component: WritingComponent,
      },
    ]
  },

  {
    path:  'gallery',
    component:  GalleryComponent,
  },
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' })
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})
export class AppRoutingModule {}
