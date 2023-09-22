import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { DataService } from '../data.service';
import { GalleryItem } from '../models/galleryItem';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss'],
  providers: [DataService]
})
export class GalleryComponent implements OnInit, OnDestroy {

  DEFAULT_LIMIT: number = 10;

  gallery: GalleryItem[] = [];
  limit: number = this.DEFAULT_LIMIT;
  offset: number = 0;

  subscription: Subscription;

  constructor(
    private activatedRouter: ActivatedRoute,
    private router: Router,
    private dataService: DataService) {}

  ngOnInit() {
    this.subscription = this.activatedRouter.paramMap.subscribe(() => {
      this.dataService.getGallery(this.limit.toString(), this.offset.toString())
        .subscribe(gallery => {
          this.gallery = gallery;
      });
    });
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
