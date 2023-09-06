import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { env } from 'src/environments/env';

@Injectable({
  providedIn: 'root'
})
export class InstructorService {
  private apiUrl = env.apiURL; // Adjust this to your API URL
  
  constructor(private http: HttpClient) {}

  // Helper function to handle errors
  private handleError(error: any) {
    console.error('API Error:', error);
    return throwError(error);
  }

  // Method for instructor login
  loginInstructor(email: string, password: string): Observable<any> {
    const loginData = { email, password };

    // Make a POST request to your login endpoint for instructors
    return this.http
      .post<any>(`${this.apiUrl}/instructors/login/`, loginData)
      .pipe(catchError(this.handleError));
  }

  // Method for instructor registration
  signupInstructor(signupData: any): Observable<any> {
    // Make a POST request to your registration endpoint for instructors
    return this.http
      .post<any>(`${this.apiUrl}/instructors/add/`, signupData)
      .pipe(catchError(this.handleError));
  }
}
