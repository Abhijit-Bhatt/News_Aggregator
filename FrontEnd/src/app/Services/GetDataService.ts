import { Injectable } from '@angular/core'

import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class GetDataService{

    flaskUrl: string = 'http://127.0.0.1:5000/display_content/'

    constructor(private httpService: HttpClient){}

    getData(searchFor, sources, language): Observable<JSON>  {
        
        let urlWithParams: string = this.flaskUrl +  `${searchFor}&${sources}&${language}&on&None`
        return this.httpService.get<JSON>(urlWithParams)
    }

}