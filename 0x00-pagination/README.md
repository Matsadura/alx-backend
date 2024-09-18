### Paginating a Dataset with Simple `page` and `page_size` Parameters

Pagination breaks a large dataset into smaller "pages" to make it easier to retrieve and display data efficiently. A common method is to use `page` and `page_size` parameters to fetch specific parts of the data.

#### 1. Simple Pagination with `page` and `page_size` Parameters

In this approach:
- `page` specifies which page of data to fetch.
- `page_size` specifies how many items should be returned per page.

#### Example Logic:
- `offset = (page - 1) * page_size`: This formula determines how many items to skip based on the requested page.
- Limit the results to `page_size`.

#### Example in Python (assuming an SQL-like dataset):
```python
def paginate_simple(dataset, page, page_size):
    offset = (page - 1) * page_size
    return dataset[offset:offset + page_size]
```
- **`page=1`** and **`page_size=10`** returns items 0 to 9.
- **`page=2`** and **`page_size=10`** returns items 10 to 19.

---

### Paginating a Dataset with Hypermedia Metadata

**Hypermedia pagination** adds metadata to the response to make it easier for clients to navigate the dataset. This typically includes links to the **next**, **previous**, **first**, and **last** pages of results.

#### Example Response Format:
```json
{
  "page": 2,
  "page_size": 10,
  "total_items": 100,
  "data": [...],
  "links": {
    "first": "/items?page=1&page_size=10",
    "prev": "/items?page=1&page_size=10",
    "next": "/items?page=3&page_size=10",
    "last": "/items?page=10&page_size=10"
  }
}
```

#### Example Logic:
```python
def paginate_hypermedia(dataset, page, page_size):
    total_items = len(dataset)
    total_pages = (total_items + page_size - 1) // page_size  # Calculate total pages
    
    offset = (page - 1) * page_size
    data = dataset[offset:offset + page_size]
    
    links = {
        "first": f"/items?page=1&page_size={page_size}",
        "prev": f"/items?page={max(1, page-1)}&page_size={page_size}",
        "next": f"/items?page={min(total_pages, page+1)}&page_size={page_size}",
        "last": f"/items?page={total_pages}&page_size={page_size}"
    }
    
    return {
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "data": data,
        "links": links
    }
```

#### Hypermedia Advantages:
- Provides clear navigation for clients to jump between pages without manually calculating page numbers.
- Offers more control over how pagination is presented to users.

---

### Deletion-Resilient Pagination

In deletion-resilient pagination, the goal is to ensure that the dataset pagination does not break or shift due to the deletion of records. A common approach is **cursor-based pagination**, where each page request includes a reference (or cursor) to the last item fetched rather than a fixed page number.

#### Key Points:
- Instead of `page` and `page_size`, cursor-based pagination uses a **cursor** (e.g., a unique ID or timestamp) to mark where the next page should start.
- The client sends the last item’s cursor with the next page request, ensuring stable pagination even if records are deleted or added in between.

#### Example:
```python
def paginate_cursor(dataset, cursor, page_size):
    # Find the index of the cursor in the dataset
    index = next((i for i, item in enumerate(dataset) if item['id'] == cursor), None)
    
    if index is None:
        return dataset[:page_size]  # If no cursor is found, return the first page
    
    return dataset[index + 1:index + 1 + page_size]
```

In this example:
- The cursor represents the last seen item (e.g., `item['id']`).
- The next page starts right after this item, avoiding issues caused by deletions, as the cursor maintains a reference to a stable point in the dataset.

#### Advantages of Cursor-Based Pagination:
- More efficient for large datasets or systems with frequent inserts or deletions.
- Ensures consistent pagination when records are deleted, since it uses a fixed reference to the last seen item.
