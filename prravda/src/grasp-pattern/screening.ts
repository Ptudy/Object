import { Movie } from "./movie";

export class Screening {
  public reserve(movie: Movie): Reservation {
    movie.getFee();
  }
}
