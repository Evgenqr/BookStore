using BookStore.Models;
using Humanizer.Localisation;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Diagnostics;
using System.Linq;

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
        /// <summary>
        /// Вывод всех книг
        /// </summary>
        [HttpGet]
        public IActionResult GetBooks()
        {
            return Ok(_context.Books.ToList());
        }
        /// <summary>
        /// Вывод книги по Id
        /// </summary>
        [HttpGet("{id}")]
        public IActionResult GetBooks(long id)
        {
            var book = _context.Books.FirstOrDefault(x => x.Id == id);
            if (book == null)
            {
                return NotFound();
            }
            return Ok(book);
        }
        /// <summary>
        /// Добавление новой книги
        /// </summary>
        [HttpPost]
        public IActionResult AddBook([FromBody] Book book)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            var author = _context.Authors.FirstOrDefault(a => a.Id == book.AuthorId);
            var genre = _context.Genres.FirstOrDefault(g => g.Id == book.GenreId);
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
        /// <summary>
        /// Обновление книги
        /// </summary>
        [HttpPut("{id}")]
        public IActionResult UpdateBook(long id, [FromBody] Book book)
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
        /// <summary>
        /// Удаление книги
        /// </summary>
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
        /// <summary>
        /// Поиск книги по названию
        /// </summary>
        [HttpGet("title/{title}")]
        public IActionResult GetBooksByTitle(string title)
        {
            var books = _context.Books
                .Include(b => b.Author)
                .Include(b => b.Genre)
                .Where(b => b.Title.Contains(title))
                .ToList();
            return Ok(books);
        }
        /// <summary>
        /// Поиск книги по Id жанра
        /// </summary>
        [HttpGet("genre/{genreId}")]
        public IActionResult GetBooksByGenre(long genreId)
        {
            var books = _context.Books
                .Include(b => b.Author)
                .Include(b => b.Genre)
                .Where(b => b.GenreId == genreId)
                .ToList();
            return Ok(books);
        }
        /// <summary>
        /// Поиск книги по Id автора
        /// </summary>
        [HttpGet("author/{authorId}")]
        public IActionResult GetBooksByAuthor(long authorId)
        {
            var books = _context.Books
                .Include(b => b.Author)
                .Include(b => b.Genre)
                .Where(b => b.AuthorId == authorId)
                .ToList();
            return Ok(books);
        }
        /// <summary>
        /// Поиск книги по году издания
        /// </summary>
        [HttpGet("year/{year}")]
        public IActionResult GetBooksByYear(short year)
        {
            var books = _context.Books
                .Include(b => b.Author)
                .Include(b => b.Genre)
                .Where(b => b.Year == year)
                .ToList();
            return Ok(books);
        }
    }
}
