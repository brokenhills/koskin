import { Injectable } from '@angular/core';
import { Http, Response} from  '@angular/http';
import { environment } from '../environments/environment';
import { Observable } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import { Writing } from '../app/models/writing';
import { MainInfo } from '../app/models/mainInfo';
import { GalleryItem } from '../app/models/galleryItem';
import { NewsItem } from '../app/models/newsItem';
import { Biography } from '../app/models/biography';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  API_URL = environment.apiUrl;

  constructor(private  httpClient: Http) {}

  private handleError(error: Response | any) {
    console.log(error);
    return Observable.throw(error);
  }

  public getWritings(): Observable<Writing[]> {
    return this.httpClient
    .get(`${this.API_URL}/writings`)
    .map((response: { json: any; }) => {
      const writings = response.json;
      return writings.map((writing: Object) => new Writing(writing));
    }).catch(this.handleError);
  }

  public getWritingById(id: number): Observable<Writing> {
    return this.httpClient
    .get(`${this.API_URL}/writings/${id}`)
    .map((response: { json: any}) => {
      return new Writing(response.json);
    }).catch(this.handleError);
  }

  public getMain(): Observable<MainInfo[]> {
    return this.httpClient
    .get(`${this.API_URL}/main`)
    .map((response: { json: any}) => {
      const mainInfos = response.json;
      return mainInfos.map((mainInfo: Object) => new MainInfo(mainInfo));
    }).catch(this.handleError);
  }

  public getGallery(){
    return this.httpClient
    .get(`${this.API_URL}/gallery`)
    .map((response: {json: any}) => {
      const galleryItems = response.json;
      return galleryItems.map((item: Object) => new GalleryItem(item));
    }).catch(this.handleError);
  }

  public getBiograhy(){
    return this.httpClient
    .get(`${this.API_URL}/biography`)
    .map((response: {json: any}) => {
      const biographies = response.json;
      return biographies.map((bio: Object) => new Biography(bio));
    }).catch(this.handleError);
  }

  public getNews(){
    return this.httpClient
    .get(`${this.API_URL}/news`)
    .map((response: {json: any}) => {
      const news = response.json;
      return news.map((item: Object) => new NewsItem(item));
    });
  }

  //TODO: contacts empty in DB now.
  public getContacts(){
      return this.httpClient.get(`${this.API_URL}/contact`);
  }
}
