using BookStore.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace BookStore.Controllers
{
    [ApiController]
    [Route("/api/[controller]")]
    public class AuthorController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public AuthorController(ApplicationDbContext context)
        {
            _context = context;
        }
        /// <summary>
        /// Вовод всех жанров
        /// </summary>
        [HttpGet]
        public IActionResult GetAuthors()
        {
            return Ok(_context.Authors.ToList());
        }
        /// <summary>
        /// Вывод автора по Id
        /// </summary>
        [HttpGet("{id}")]
        public IActionResult GetAuthors(int id)
        {
            var author = _context.Authors.FirstOrDefault(x => x.Id == id);
            if (author == null)
            {
                return NotFound();
            }
            return Ok(author);
        }
        /// <summary>
        /// Добавление автора 
        /// </summary>
        [HttpPost]
        public IActionResult AddAuthor([FromBody] Author author)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            _context.Set<Author>().Add(author);
            _context.SaveChanges();
            return Ok();
        }
        /// <summary>
        /// Обновление автора 
        /// </summary>
        [HttpPut("{id}")]
        public IActionResult UpdateAuthor(int id, [FromBody] Author author)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            var editAuthor = _context.Authors.FirstOrDefault(b => b.Id == id);
            if (editAuthor == null)
            {
                return NotFound();
            }
            editAuthor.FullName = author.FullName;
            editAuthor.DateOfBirth = author.DateOfBirth;
            _context.Update(editAuthor);
            _context.SaveChanges();
            return Ok();
        }
        /// <summary>
        /// Удаление автора 
        /// </summary>
        [HttpDelete("{id}")]
        public IActionResult DeleteAuthor(int id)
        {
            var author = _context.Authors.FirstOrDefault(x => x.Id == id);
            if (author is null)
            {
                return NotFound();
            }
            _context.Remove(author);
            _context.SaveChanges();
            return Ok();
        }




    }
}
