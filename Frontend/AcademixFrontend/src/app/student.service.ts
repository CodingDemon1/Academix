import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { env } from 'src/environments/env';

@Injectable({
  providedIn: 'root'
})
export class StudentService {
  private apiUrl = env.apiURL; // Adjust this to your API URL

  constructor(private http: HttpClient) {}

  // Helper function to handle errors
  private handleError(error: any) {
    console.error('API Error:', error);
    return throwError(error);
  }

  // Method for student login
  loginStudent(email: string, password: string): Observable<any> {
    const loginData = { email, password };

    // Make a POST request to your login endpoint
    return this.http
      .post<any>(`${this.apiUrl}/students/login/`, loginData)
      .pipe(catchError(this.handleError));
  }

  // Method for student registration
  signupStudent(signupData: any): Observable<any> {
    // Make a POST request to your registration endpoint
    return this.http
      .post<any>(`${this.apiUrl}/students/add/`, signupData)
      .pipe(catchError(this.handleError));
  }
}
