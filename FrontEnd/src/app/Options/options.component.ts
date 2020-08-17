import { Component, OnInit, Injectable} from '@angular/core';

import { FormControl } from '@angular/forms'
import { GetDataService } from '../services/GetDataService'
import {MatDialog} from '@angular/material/dialog'

interface Action {
  value: string
  viewValue: string
}

@Component({
  selector: 'app-options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.scss']
})

@Injectable({
  providedIn: 'root'
})
export class OptionsComponent{

  // Display content 
  load: boolean

  // All parameters to enter
  searchParameters: string
  language: string

  selectedSources = new FormControl()
  sourcesList: string[] = ['cnn', 'fox-news', 'nbc-news']

  actionList: Action[] = [{value:'getTopHeadlines', viewValue:'Get Top Headlines'}, {value:'getEverything', viewValue:'Get Everything'}]
  selectedAction: string

  // Data that is retreived from backend
  data: JSON

  constructor(private getData: GetDataService, public dialog: MatDialog) {
    this.load = false
   }

  
  openDialog() {
    
    const dialogRef = this.dialog.open(Infobox);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }


  getter(){
    
    console.log(`${this.searchParameters} ${this.selectedSources.value} ${this.language} ${this.selectedAction}`)

   this.getData.getData(this.searchParameters, this.selectedSources.value, this.language, this.selectedAction).subscribe({
      next: (data) => {
        this.data = data
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

@Component({
  selector: 'info-box',
  templateUrl: 'infobox.html'
})
export class Infobox{}
