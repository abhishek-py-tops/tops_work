# What is a QuerySet?Write program to create a new Post object in database:

# A QuerySet in Django is a collection of database queries that represents a set of objects (rows in a table).

# Lazy (doesn't hit the database until needed),

# Used for retrieving, filtering, ordering, updating, and deleting data from the database.

# # Get all posts
# all_posts = Post.objects.all()

# # Filter posts
# recent_posts = Post.objects.filter(title__icontains="First")

# # Get single post
# single_post = Post.objects.get(id=1)



