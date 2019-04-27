class Review:

    all_reviews = []

    def __init__(self,id,blog,submitted_by,posted,review):
        self.id = id
        self.blog = blog
        self.submitted_by = submitted_by
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.blog_id == id:
                response.append(review)

        return response