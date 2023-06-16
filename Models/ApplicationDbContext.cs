using BookStore.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Diagnostics;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Options;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace BookStore.Models
{
    public class ApplicationDbContext: DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        { 
        }
        // Связываем сущности (модели) с таблицами в базе данных TestModel
        public DbSet<Book> Books { get; set; }
        public DbSet<Author> Authors { get; set; }
        public DbSet<Genre> Genres { get; set; }
        // Настройки подключения к БД
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer("Server=(localdb)\\mssqllocaldb;Database=BookStore;Trusted_Connection=True;");
            optionsBuilder.ConfigureWarnings(warnings => warnings.Throw(CoreEventId.InvalidIncludePathError));
        }
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Genre>().HasKey(g => new { g.Id });
            modelBuilder.Entity<Author>().HasKey(a => new { a.Id });
            modelBuilder.Entity<Book>().HasKey(b => new { b.Id });

            modelBuilder.Entity<Author>()
                .HasMany(a => a.AuthorGenres)
                .WithMany(a => a.GenreAuthors);

            modelBuilder.Entity<Genre>()
                .HasMany(g => g.GenreAuthors)
                .WithMany(g => g.AuthorGenres);
        }
    }
   
       
}

