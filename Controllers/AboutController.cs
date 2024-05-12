using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using SeyahatProje.Models.Sınıflar;

namespace SeyahatProje.Controllers
{
    public class AboutController : Controller
    {
        // GET: About
        Context c = new Context();
        public ActionResult Index()
        {
            var degerler= c.Hakkımızdas.ToList();
            
            
            return View(degerler);

        }
    }
}