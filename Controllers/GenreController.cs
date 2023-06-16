using BookStore.Models;
using Humanizer.Localisation;
using Microsoft.AspNetCore.Mvc;

namespace BookStore.Controllers
{
    [ApiController]
    [Route("/api/[controller]")]
    public class GenreController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public GenreController(ApplicationDbContext context)
        {
            _context = context;
        }
        /// <summary>
        /// Вывод всех жанров
        /// </summary>
        [HttpGet]
        public IActionResult GetGenres()
        {
            return Ok(_context.Genres.ToList());
        }
        /// <summary>
        /// Вывод жанра по Id
        /// </summary>
        [HttpGet("{id}")]
        public IActionResult GetGenres(int id)
        {
            var genre = _context.Genres.FirstOrDefault(x => x.Id == id);
            if (genre == null)
            {
                return NotFound();
            }
            return Ok(genre);
        }
        /// <summary>
        /// Добавление нового жанра 
        /// </summary>
        [HttpPost]
        public IActionResult AddGenre(Genre genre)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            _context.Set<Genre>().Add(genre);
            _context.SaveChanges();
            return Ok();
        }
        /// <summary>
        /// Обновление жанра 
        /// </summary>
        [HttpPut("{id}")]
        public IActionResult UpdateGenre(int id, [FromBody] Genre genre)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            var editGenre = _context.Genres.FirstOrDefault(b => b.Id == id);
            if (editGenre == null)
            {
                return NotFound();
            }
            editGenre.GenreName = genre.GenreName;
            _context.Update(editGenre);
            _context.SaveChanges();
            return Ok();
        }
        /// <summary>
        /// Удаление жанра 
        /// </summary>
        [HttpDelete("{id}")]
        public IActionResult DeleteGenre(int id)
        {
            var genre = _context.Genres.FirstOrDefault(x => x.Id == id);
            if (genre is null)
            {
                return NotFound();
            }
            _context.Remove(genre);
            _context.SaveChanges();
            return Ok();
        }

    }
}
