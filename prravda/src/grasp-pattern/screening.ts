import { Movie } from "./movie";

export class Screening {
  public reserve(movie: Movie) {
    movie.getFee();
  }
}
