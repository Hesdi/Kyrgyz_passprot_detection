package javaprojsait.controllers;

import javaprojsait.models.Post;
import javaprojsait.repositore.postrepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class regcontrollers {
    @Autowired
    private postrepository Postrepository;
    @GetMapping("/reg")
    public String regmain(Model model){
        Iterable<Post> posts = Postrepository.findAll();
        model.addAttribute("posts",posts);
        return "reg-main";
    }
}
