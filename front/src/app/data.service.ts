import { Injectable } from '@angular/core';
import { ApiService } from '../app/api.service'
import { Observable } from 'rxjs';
import { Writing } from '../app/models/writing';
import { GalleryItem } from './models/galleryItem';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private api: ApiService) { }

  getWritings(limit: string, offset: string): Observable<Response> {
    return this.api.getWritings(limit, offset);
  }

  getWriting(id: string): Observable<Writing> {
    return this.api.getWritingById(id);
  }

  getGallery(): Observable<GalleryItem[]> {
    return this.api.getGallery();
  }
}
