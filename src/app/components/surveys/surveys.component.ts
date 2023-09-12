import { Component, ViewChild, ViewEncapsulation } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AgGridAngular } from 'ag-grid-angular';
import { CellClickedEvent, ColDef, GridReadyEvent } from 'ag-grid-community';
import { AgGridModule } from 'ag-grid-angular';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { MatCardModule } from '@angular/material/card';
import { faker } from "@faker-js/faker";

@Component({
  selector: 'app-surveys',
  standalone: true,
  imports: [CommonModule, AgGridModule, MatCardModule],
  templateUrl: './surveys.component.html',
  styleUrls: ['./surveys.component.scss']
})
export class SurveysComponent {
  // Each Column Definition results in one Column.
  public columnDefs: ColDef[] = [
    { field: 'id'},
    { field: 'make'},
    { field: 'model'},
    { field: 'price'},
    { field: 'available'},
    { field: 'date'},
    { field: 'comments'}
  ];

  // DefaultColDef sets props common to all Columns
  public defaultColDef: ColDef = {
    editable: true,
    sortable: true,
    filter: true,
    resizable: true,
  };

  // Data that gets displayed in the grid
  public rowData$!: Observable<any[]>;

  // For accessing the Grid's API
  @ViewChild(AgGridAngular) agGrid!: AgGridAngular;

  constructor( private http: HttpClient ) {
  }

  // Example load data from server
  onGridReady(params: GridReadyEvent) {
    this.http
      .get<any[]>('https://www.ag-grid.com/example-assets/row-data.json')
      .subscribe((data) => {
        let id = 1;
        data.forEach((element) => {
          id ++;
          element.id = id;
          element.available = true;
          element.date = new Date(+(new Date()) - Math.floor(Math.random() * 10000000000));
          element.comments = faker.company.catchPhrase()
        })
        this.rowData$ = of(data);
      })
  }

    // Example of consuming Grid Event
    onCellClicked( e: CellClickedEvent): void {
      console.log('cellClicked', e);
    }

    // Example using Grid's API
    clearSelection(): void {
      this.agGrid.api.deselectAll();
    }
}
