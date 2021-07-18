import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { WritingsComponent } from './writings/writings.component';
import { AppRoutingModule } from  './app-routing/app-routing.module';
import { WritingComponent } from './writing/writing.component';
import { HttpClientModule } from '@angular/common/http';
import { GalleryComponent } from './gallery/gallery.component';
import { MainComponent } from './main/main.component';

@NgModule({
  declarations: [
    AppComponent,
    WritingsComponent,
    WritingComponent,
    GalleryComponent,
    MainComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
