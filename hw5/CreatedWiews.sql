CREATE VIEW IF NOT EXISTS GenreStatsByCity AS
SELECT
    customers.City AS City,
    genres.Name AS Genre,
    COUNT(invoices.InvoiceId) AS purchase_count,
    RANK() OVER (PARTITION BY genres.Name ORDER BY COUNT(invoices.InvoiceId) DESC) AS rank_position
FROM customers
JOIN invoices ON customers.CustomerId = invoices.CustomerId
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
JOIN tracks ON invoice_items.TrackId = tracks.TrackId
JOIN genres ON tracks.GenreId = genres.GenreId
GROUP BY customers.City, genres.Name;
