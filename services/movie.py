from models.movie import Movie as MovieModel



class MovieService():
    def __init__(self, db):
        self.db = db
        
        
    def get_movies(self):
        mv = self.db.query(MovieModel).all()
        return mv
    
    def get_movie(self, id):
        mv = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return mv
    
    def get_movies_by_category(self, category, year):
        mv = self.db.query(MovieModel).filter(MovieModel.category == category and MovieModel.year == year).all()
        return mv
    
    def create_movie(self, movie):
        mv = MovieModel(**movie.model_dump())
        self.db.add(mv)
        self.db.commit()
        return mv
    
    def update_movie(self, id, movie):
        mv = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        mv.title = movie.title
        mv.overview = movie.overview
        mv.year = movie.year
        mv.rating = movie.rating
        mv.category = movie.category
        self.db.commit()
        return mv
    
    def delete_movie(self, id):
        
        mv = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not mv:
            return False
        else:
            self.db.delete(mv)
            self.db.commit()
            return True
        