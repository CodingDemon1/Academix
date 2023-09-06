import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private userRole: string = '';

  setUserRole(role: string) {
    this.userRole = role;
  }

  getUserRole(): string {
    return this.userRole;
  }
}
