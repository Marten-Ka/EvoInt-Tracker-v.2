<script lang="ts">
	export let img_source: string;
	export let img_height: string;
	export let img_alt: string;
	export let reference: string;
	export let source_link: string;
	export let source_text: string;
	export let heading: string;
	export let publication_date: string;
	export let author: string;
	export let content: string;
</script>

<div class="mb-6 h-full lg:mb-0">
	<div class="relative block bg-white rounded-lg shadow-lg">
		<div class="flex justify-center">
			<div
				class="relative group overflow-hidden bg-no-repeat bg-cover shadow-lg rounded-lg mx-4 -mt-4"
				data-mdb-ripple="true"
				data-mdb-ripple-color="light"
			>
				<img src={img_source} class={img_height} alt={img_alt} />
				<a href={reference}>
					<div
						class="absolute top-0 right-0 bottom-0 left-0 w-full h-full overflow-hidden bg-fixed opacity-0 hover:opacity-100 transition duration-300 ease-in-out"
						style="background-color: rgba(251, 251, 251, 0.15)"
					/>
				</a>
				<a
					href={source_link}
					target="_blank"
					class="source opacity-0 bottom-0 left-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1 "
				>
					{source_text}
				</a>
			</div>
		</div>
		<div class="flex flex-col justify-center p-2 md:p-6">
			<h5 class="font-bold text-2xl mb-1 2xl:mb-3">{heading}</h5>
			<p class="text-gray-500 mb-2 2xl:mb-4">
				<small
					>Veröffentlicht am <u>{publication_date}</u> von
					<p class="text-gray-900">{author}</p></small
				>
			</p>
			<p class="mb-4 pb-2 text-base 2xl:text-lg w-full 2xl:w-[75%] place-self-center">{content}</p>
			<a
				href={reference}
				data-mdb-ripple="true"
				data-mdb-ripple-color="light"
				class="inline-block px-6 py-2.5 w-auto place-self-center bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
				>Read more</a
			>
		</div>
	</div>
</div>

<style lang="postcss">
	@media only screen and (hover: none) and (pointer: coarse) {
		.source {
			opacity: 80;
		}
	}
</style>
