// auth.service.ts
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  getToken(): string | null {
    return localStorage.getItem('token');
  }

  getUser(): any | null {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  }

  isLoggedIn(): boolean {
    // Check if a valid token is present (you can also check the expiration date here)
    return !!this.getToken();
  }
  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  }
}
