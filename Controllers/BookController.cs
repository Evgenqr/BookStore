using BookStore.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Diagnostics;

namespace BookStore.Controllers
{
    [ApiController]
    [Route("/api/[controller]")]
    public class BookController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public BookController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult GetBooks()
        {
            return Ok(_context.Books.ToList());
        }
        [HttpGet("{id}")]
        public IActionResult GetBooks(int id)
        {
            var book = _context.Books.FirstOrDefault(x => x.Id == id);
            if (book == null)
            {
                return NotFound();
            }
            return Ok(book);
        }

        [HttpPost]
        public IActionResult AddBooks([FromBody] Book book)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            var author = _context.Authors.FirstOrDefault(a => a.Id == book.AuthorId);
            var genre = _context.Genres.FirstOrDefault(a => a.Id == book.GenreId);
            var newBook = new Book
            {
                Author = author,
                AuthorId = book.AuthorId,
                Description = book.Description,
                Genre = genre,
                Title = book.Title,
                GenreId = book.GenreId,
                Year = book.Year
            };

            _context.Books.Add(newBook);
            _context.SaveChanges();
            return Ok();
           
        }

        [HttpPut("{id}")]
        public IActionResult UpdateBook(int id, [FromBody] Book book)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            var author = _context.Authors.FirstOrDefault(a => a.Id == book.AuthorId);
            var genre = _context.Genres.FirstOrDefault(a => a.Id == book.GenreId);
            var editBook = _context.Books.FirstOrDefault(b => b.Id == id);

            if (editBook == null)
            {
                return NotFound();
            }
            editBook.Author = author;
            editBook.AuthorId = book.AuthorId;
            editBook.Description = book.Description;
            editBook.Genre = genre;
            editBook.Title = book.Title;
            editBook.GenreId = book.GenreId;
            editBook.Year = book.Year;
            _context.Update(editBook);
            _context.SaveChanges();
            return Ok();
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteBook(int id)
        {
            var book = _context.Books.FirstOrDefault(x => x.Id == id);
            if (book is null) 
            {
                return NotFound();
            }
            _context.Remove(book);
            _context.SaveChanges();
            return Ok();
        }

    }
}
