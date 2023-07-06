import { Injectable } from '@angular/core';
import { Subject,Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class EmpdataserviceService {
  private dataUpdatedSource = new Subject<any>();
  dataUpdated$ = this.dataUpdatedSource.asObservable();
  private baseUrl = 'http://127.0.0.1:8000/';

  updateData(data: any) {
    this.dataUpdatedSource.next(data);
  }
  constructor(private http: HttpClient) { }
  
  getEmployees(): Observable<any> {
    return this.http.get<any>(this.baseUrl + 'employees/');
  }

  getEmployeeDetails(id: number): Observable<any> {
    return this.http.get<any>(this.baseUrl + 'employees/' + id + '/');
  }

  addEmployee(employee: any): Observable<any> {
    return this.http.post<any>(this.baseUrl + 'employees/add/', employee);
  }

  updateEmployee(id: number, employee: any): Observable<any> {
    return this.http.put<any>(this.baseUrl + 'employees/edit/' + id + '/', employee);
  }

  updateEmployee1(id: number, employee: any): Observable<any> {
    return this.http.patch<any>(this.baseUrl + 'employees/edit/' + id + '/', employee);
  }

  deleteEmployee(id: number): Observable<any> {
    return this.http.delete<any>(this.baseUrl + 'employees/delete/' + id + '/');
  }
}
