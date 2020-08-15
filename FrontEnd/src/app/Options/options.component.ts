import { Component, OnInit, Injectable } from '@angular/core';

import { GetDataService } from '../services/GetDataService'



@Component({
  selector: 'app-options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.scss']
})

@Injectable({
  providedIn: 'root'
})
export class OptionsComponent implements OnInit {

  load: boolean
  searchParameters: string
  sources: string
  language: string

  data: JSON

  constructor(private getData: GetDataService) {
    this.load = false
   }

  ngOnInit(): void {
  }

  title = 'frontEndNewsAgg';


  getter(){
    console.log(`${this.searchParameters} ${this.sources} ${this.language}`)

   this.getData.getData(this.searchParameters, this.sources, this.language).subscribe({
      next: (data) => {
        this.data = data[""]
        console.log(this.data)
      },
      error: err => {
        console.log("Not Working!")
        console.log(err) 
      }
    })


    this.load = true


  }

  
}
