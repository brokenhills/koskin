import { Injectable } from '@angular/core';
import { ApiService } from '../app/api.service'
import { Observable } from 'rxjs';
import { Writing } from '../app/models/writing';
import { GalleryItem } from './models/galleryItem';
import { MainInfo } from './models/mainInfo';
import { HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private api: ApiService) {}

  getWritings(params: HttpParams): Observable<Response> {
    return this.api.getWritings(params);
  }

  getWriting(id: string): Observable<Writing> {
    return this.api.getWritingById(id);
  }

  getGallery(limit: string, offset: string): Observable<GalleryItem[]> {
    return this.api.getGallery(limit, offset);
  }

  getMainItems(limit: string, offset: string): Observable<MainInfo[]> {
    return this.api.getMain(limit, offset);
  }
}
