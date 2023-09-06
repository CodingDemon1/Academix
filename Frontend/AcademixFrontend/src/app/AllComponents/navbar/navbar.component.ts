import { Component, OnInit } from '@angular/core';
import { Route, Router } from '@angular/router';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  loggedInUser !: object;
  isLoggedIn : boolean = false;
  constructor(private authService: AuthService, private router : Router ){}
  
  ngOnInit(): void {
      if(this.authService.isLoggedIn()){
        this.isLoggedIn = true
        this.loggedInUser = this.authService.getUser().name;
      }
  }

  logOutUser(){
    this.isLoggedIn = false
    this.authService.logout()
    this.router.navigate([''])
  }

}
