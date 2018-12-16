import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';

import { Observable, of } from 'rxjs';

import { Data } from './data';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({ providedIn: 'root'})
export class DataService {

  private dataUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  getDataList(): Observable<Data[]> {
    return this.http.get<Data[]>(this.dataUrl+'/cache');
  }

  getData(id: string): Observable<Data> {
    const url = `${this.dataUrl}/cache/${id}`;
    return this.http.get<Data>(url)
    .pipe(
      catchError(this.handleError<Data>(`getData id=${id}`))
    );
  }

  updateData (data: Data): Observable<any> {
    return this.http.put(this.dataUrl+'/cache', data, httpOptions).pipe(
      catchError(this.handleError<any>('updateData'))
    );
  }


  get(state: number,beginYear: number,endYear: number): Observable<Data> {
    const url = `${this.dataUrl}/${state}/${beginYear}/${endYear}`;
    return this.http.get<Data>(url)
    .pipe(
      catchError(this.handleError<Data>(`getData`))
    );
  }

  deleteData(data: Data | string): Observable<Data> {
    const id = typeof data === 'string' ? data : data.id;
    const url = `${this.dataUrl}/cache/${id}`;

    return this.http.delete<Data>(url, httpOptions).pipe(catchError(this.handleError<Data>('deleteData')));
  }

  searchData(term: string): Observable<Data[]> {
    if (!term.trim()) {
      return of([]);
    }
    return this.http.get<Data[]>(`${this.dataUrl}/cache?name=${term}`).pipe(
      catchError(this.handleError<Data[]>('searchData', []))
    );
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

}
