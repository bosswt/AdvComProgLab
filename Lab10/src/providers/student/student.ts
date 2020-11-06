import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Student } from "../../models/student.model";

/*
  Generated class for the StudentProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class StudentProvider {
  private url = "http://localhost:5000/findscore?id=";
  constructor(public http: HttpClient) {
    console.log("Hello StudentProvider Provider");
  }
  public getScore(id: string) {
    console.log(id);
    return this.http.get<Student>(this.url + id);
  }
}
