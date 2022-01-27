import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from  '@angular/common/http';
import { environment } from '../environments/environment.prod';
import { Observable } from 'rxjs';
import { Writing } from '../app/models/writing';
import { MainInfo } from '../app/models/mainInfo';
import { GalleryItem } from '../app/models/galleryItem';
import { NewsItem } from '../app/models/newsItem';
import { Biography } from '../app/models/biography';
import { map } from 'rxjs/operators';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  API_URL = environment.apiUrl;

  HEADERS: HttpHeaders = new HttpHeaders({
    'Authorization': 'Negotiate'
  });

  params: HttpParams = new HttpParams();

  constructor(private  httpClient: HttpClient) {}

  private handleError(error: Response | any) {
    console.log(error);
    return throwError(error);
  }

  public getWritings(params: HttpParams): Observable<Response> {
    let headers: HttpHeaders = new HttpHeaders({
      'Authorization': 'Negotiate'
    });
    return this.httpClient
    .get(`${this.API_URL}/writings/`, { headers, params }).pipe(
      map((response: Response) => {
        return response;
      }),
      catchError(this.handleError)
    );
  }

  public getWritingById(id: string): Observable<Writing> {
    return this.httpClient
    .get(`${this.API_URL}/writings/${id}/`).pipe(
    map((response: Object) => {
      return new Writing(response);
    }),
    catchError(this.handleError));
  }

  public getMain(limit: string, offset: string): Observable<MainInfo[]> {
    return this.httpClient
    .get(`${this.API_URL}/main/?limit=${limit}&offset=${offset}`).pipe(
    map((response: Array<Object>) => {
      return response['results'].map((mainInfo: Object) => new MainInfo(mainInfo));
    }),
    catchError(this.handleError));
  }

  public getGallery(limit: string, offset: string){
    let headers: HttpHeaders = new HttpHeaders({
      'Authorization': 'Negotiate'
    });
    return this.httpClient
    .get(`${this.API_URL}/gallery/?limit=${limit}&offset${offset}`, { headers }).pipe(
    map((response: Array<Object>) => {
      return response['results'].map((item: Object) => new GalleryItem(item));
    }),
    catchError(this.handleError));
  }

  public getBiograhy(){
    return this.httpClient
    .get(`${this.API_URL}/biography/`).pipe(
    map((response: {json: any}) => {
      const biographies = response.json;
      return biographies['results'].map((bio: Object) => new Biography(bio));
    }),
    catchError(this.handleError));
  }

  public getNews(){
    return this.httpClient
    .get(`${this.API_URL}/news/`).pipe(
    map((response: {json: any}) => {
      const news = response.json;
      return news['results'].map((item: Object) => new NewsItem(item));
    }),
    catchError(this.handleError));
  }

  //TODO: contacts empty in DB now.
  public getContacts(){
      return this.httpClient.get(`${this.API_URL}/contact/`).pipe();
  }
}
