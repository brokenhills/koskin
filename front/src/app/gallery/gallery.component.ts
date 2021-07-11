import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { GalleryItem } from '../models/galleryItem';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss']
})
export class GalleryComponent implements OnInit {

  gallery: GalleryItem[] = [];

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getGallery()
    .subscribe(gallery => {
      this.gallery = gallery;
    });
  }

}
