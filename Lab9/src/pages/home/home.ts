import { Component } from "@angular/core";
import { NavController } from "ionic-angular";
import { ClickBlock } from "ionic-angular/umd/components/app/click-block";

@Component({
  selector: "page-home",
  templateUrl: "home.html",
})
export class HomePage {
  url: string;
  imageUrl: string;
  constructor(public navCtrl: NavController) {}
  click() {
    this.imageUrl = this.url;
  }
}
