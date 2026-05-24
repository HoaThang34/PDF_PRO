import { useState } from 'react'

const faqs = [
  { q: 'PDF PRO có miễn phí không?', a: 'Có! PDF PRO có gói miễn phí với đầy đủ các tính năng cơ bản. Bạn có thể merge, split, nén và chuyển đổi PDF hoàn toàn miễn phí.' },
  { q: 'Có giới hạn dung lượng file không?', a: 'Gói miễn phí hỗ trợ file tối đa 50MB. Gói Pro hỗ trợ lên tới 2GB và không giới hạn số lượng file xử lý mỗi ngày.' },
  { q: 'File của tôi có bị lưu lại không?', a: 'File của bạn được tự động xóa khỏi server sau 24 giờ. Chúng tôi cam kết không đọc, lưu trữ hoặc chia sẻ dữ liệu của bạn với bất kỳ bên thứ ba nào.' },
  { q: 'PDF PRO có hỗ trợ OCR không?', a: 'Có! Tính năng OCR AI giúp nhận dạng văn bản từ hình ảnh scan với độ chính xác cao. Tính năng này có sẵn trên gói Pro và Business.' },
  { q: 'Có API để tích hợp không?', a: 'Có! PDF PRO cung cấp API đầy đủ cho phép bạn tích hợp xử lý PDF vào ứng dụng của mình. API có sẵn trên gói Pro và Business.' },
]

function FAQItem({ faq, open, onClick }) {
  return (
    <div className={`faq-item ${open ? 'faq-item--open' : ''}`}>
      <button className="faq-question" onClick={onClick}>
        <span>{faq.q}</span>
        <span className="faq-arrow">{open ? '−' : '+'}</span>
      </button>
      <div className="faq-answer" style={{ maxHeight: open ? 200 : 0 }}>
        <p>{faq.a}</p>
      </div>
    </div>
  )
}

export default function FAQ() {
  const [openIndex, setOpenIndex] = useState(null)

  return (
    <section className="faq" id="faq">
      <div className="container">
        <div className="section-header">
          <h2>Câu hỏi thường gặp</h2>
          <p>Giải đáp mọi thắc mắc về PDF PRO</p>
        </div>
        <div className="faq-list">
          {faqs.map((faq, i) => (
            <FAQItem
              key={i}
              faq={faq}
              open={openIndex === i}
              onClick={() => setOpenIndex(openIndex === i ? null : i)}
            />
          ))}
        </div>
      </div>
    </section>
  )
}
