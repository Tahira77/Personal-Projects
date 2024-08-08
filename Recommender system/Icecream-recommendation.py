class IceCreamRecommendationSystem:
    def __init__(self):
        self.user_ratings = {
            'Alice': {'strawberry': 3, 'chocolate': 4, 'vanilla': 1, 'mint': 4, 'caramel': 3},
            'Bob': {'strawberry': 3, 'chocolate': 1, 'vanilla': 2, 'mint': 2, 'caramel': 3},
            'Charlie': {}  # Ratings for user Charlie will be added later
        }

    def add_user_ratings(self, user, ratings):
        if user not in self.user_ratings:
            print("User not found.")
            return
        self.user_ratings[user] = ratings

    def recommend_ice_cream(self, user):
        if user not in self.user_ratings:
            print("User not found.")
            return

        # Print ratings of users Alice and Bob
        print("Ratings of users Alice and Bob:")
        print("{:<10} {:<15} {:<15}".format("Flavor", "Alice", "Bob"))
        for flavor in self.user_ratings['Alice']:
            print("{:<10} {:<15} {:<15}".format(flavor, self.user_ratings['Alice'][flavor], self.user_ratings['Bob'][flavor]))

        # Calculate average ratings for each flavor
        avg_ratings = {}
        for flavor in self.user_ratings['Alice']:
            ratings = []
            if flavor in self.user_ratings['Alice']:
                ratings.append(self.user_ratings['Alice'][flavor])
            if flavor in self.user_ratings['Bob']:
                ratings.append(self.user_ratings['Bob'][flavor])
            if flavor in self.user_ratings['Charlie']:
                ratings.append(self.user_ratings['Charlie'][flavor])

            if ratings:
                avg_ratings[flavor] = sum(ratings) / len(ratings)

        # Recommend the flavor with the highest average rating
        if avg_ratings:
            recommended_flavor = max(avg_ratings, key=avg_ratings.get)
            print("\nRecommended ice cream flavor for user Charlie:")
            print(f"{recommended_flavor}")
        else:
            print("No ratings available for recommendation.")

# Create an instance of IceCreamRecommendationSystem
ice_cream_system = IceCreamRecommendationSystem()

# Adding some ratings for Charlie
ice_cream_system.add_user_ratings('Charlie', {'strawberry': 4, 'chocolate': 3, 'vanilla': 2, 'mint': 5, 'caramel': 4})

# Get a recommendation for Charlie
ice_cream_system.recommend_ice_cream('Charlie')
