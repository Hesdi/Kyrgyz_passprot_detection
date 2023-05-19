package javaprojsait.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class maincontrollers {

    @GetMapping("/index")
    public String index(Model model) {
        model.addAttribute("index","Главная страница");
        return "index";
    }
    @GetMapping("/about")
    public String about(Model model){
        model.addAttribute("about","страница про нас");
        return "about";
    }
    @GetMapping("/teashop")
    public String teashop(Model model){
        model.addAttribute("teashop","страни");
        return "teashop";
    }
    @GetMapping("/pricing")
    public String pricing(Model model){
        model.addAttribute("pricing","страни");
        return "pricing";
    }
    @GetMapping("/testimonies")
    public String testimonies(Model model){
        model.addAttribute("testimonies","страни");
        return "testimonies";
    }
    @GetMapping("/contact")
    public String contact(Model model){
        model.addAttribute("contact","страни");
        return "contact";
    }
    @GetMapping("/services")
    public String services(Model model){
        model.addAttribute("services","страни");
        return "services";
    }
}