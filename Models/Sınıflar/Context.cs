using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;
using System.Data.Entity;
namespace SeyahatProje.Models.Sınıflar
{
    public class Context : DbContext

    {
        public DbSet<Admin> Admins { get; set; }
        public DbSet<AdresBlog> AdresBlogs { get; set; }
        public DbSet<Blog> Blogs { get; set; }
        public DbSet<Hakkımızda> Hakkımızdas { get; set; }
        public DbSet<İletişim> iletişims { get; set; }
        public DbSet<Yorumlar> Yorumlars { get; set; }
        public DbSet<TarihiYerler>tarihiYerlers { get; set; }
        public DbSet<DogalGuzellikler>DogalGuzellikler { get; set; }




    }
}