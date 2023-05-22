package javaprojsait.repositore;

import org.springframework.data.repository.CrudRepository;
import javaprojsait.models.Post;

public interface postrepository extends CrudRepository<Post,Long>{
}
